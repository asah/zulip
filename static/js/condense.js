import $ from "jquery";

import { format, getUnixTime, startOfToday, fromUnixTime } from "date-fns";
import * as message_flags from "./message_flags";
import * as message_lists from "./message_lists";
import * as message_viewport from "./message_viewport";
import * as popovers from "./popovers";
import * as recent_topics_util from "./recent_topics_util";
import * as rows from "./rows";

/*
This library implements two related, similar concepts:

- condensing, i.e. cutting off messages taller than about a half
  screen so that they aren't distractingly tall (and offering a button
  to uncondense them).

- Collapsing, i.e. taking a message and reducing its height to a
  single line, with a button to see the content.

*/

const _message_content_height_cache = new Map();

export function fc_uncollapse(row, message) {
    const mbox = row.find(".messagebox");
    mbox.css("height", "");
    mbox.find(".messagebox-content").show();
    mbox.find(".message_fc_collapsed_line").hide();
    row.closest(".message_row").find(".date_row").show();
    if (row.hasClass("fc_mention_collapse")) {
        row.removeClass("fc_mention_collapse");
        row.addClass("mention");
    }
}

export function fc_collapse(row, message, datestr_cutoff) {
    // todo: performance on initial rendering - static rendering?
    // also, I left in a lot of old code for preparing content
    // which is ultimate hidden (left to avoid merge conflicts)
    row.children(".date_row").hide();
    const mbox = row.find(".messagebox").css("height", "20px");
    if (row.hasClass("mention")) {
        row.removeClass("mention");
        row.addClass("fc_mention_collapse");
    }
    const mc = mbox.children(".messagebox-content").hide();
    const fc = mbox.find(".message_fc_collapsed_line > .fc_summary");
    const fc_summary = mc.children(".rendered_markdown").text().replace(/\n/g, " ").replace(/^[♪\s-]*https?:\/\/[^ ]+[♪\s-]*/, '').substr(0,100);
    fc.text(fc_summary).parent().show();
    if (message.timestamp < datestr_cutoff) {
        const datestr = format(fromUnixTime(message.timestamp), "MMM d");
        mbox.find(".fc_message_time").text(datestr);
    }
}

function show_more_link(row) {
    row.find(".message_condenser").hide();
    row.find(".message_expander").show();
}

function show_condense_link(row) {
    row.find(".message_expander").hide();
    row.find(".message_condenser").show();
}

function condense_row(row) {
    const content = row.find(".message_content");
    content.addClass("condensed");
    if (content.hasClass("could-be-condensed")) {
        show_more_link(row);
    }
}

function uncondense_row(row) {
    const content = row.find(".message_content");
    content.removeClass("condensed");
    if (content.hasClass("could-be-condensed")) {
        show_condense_link(row);
    }
}

export function uncollapse(row) {
    // Uncollapse a message, restoring the condensed message [More] or
    // [Show less] link if necessary.
    const message = message_lists.current.get(rows.id(row));
    fc_uncollapse(row, message);
    message.collapsed = false;
    message.unread = false;
    message_flags.save_force_uncollapsed(message);

    const process_row = function process_row(row) {
        const content = row.find(".message_content");
        content.removeClass("collapsed");

        if (message.condensed === true) {
            // This message was condensed by the user, so re-show the
            // [More] link.
            condense_row(row);
        } else if (message.condensed === false) {
            // This message was un-condensed by the user, so re-show the
            // [Show less] link.
            uncondense_row(row);
        } else if (content.hasClass("could-be-condensed")) {
            // By default, condense a long message.
            condense_row(row);
        } else {
            // This was a short message, no more need for a [More] link.
            row.find(".message_expander").hide();
        }
    };

    // We also need to collapse this message in the home view
    const home_row = message_lists.home.get_row(rows.id(row));

    process_row(row);
    process_row(home_row);
}

export function collapse(row) {
    // Collapse a message, hiding the condensed message [More] or
    // [Show less] link if necessary.
    const message = message_lists.current.get(rows.id(row));
    message.unread = false;
    message.collapsed = true;
    const datestr_cutoff = getUnixTime(startOfToday());
    fc_collapse(row, message, datestr_cutoff);

    if (message.locally_echoed) {
        // Trying to collapse a locally echoed message is
        // very rare, and in our current implementation the
        // server response overwrites the flag, so we just
        // punt for now.
        return;
    }

    message_flags.save_force_collapsed(message);

    const process_row = function process_row(row) {
        row.find(".message_content").addClass("collapsed");
        show_more_link(row);
    };

    // We also need to collapse this message in the home view
    const home_row = message_lists.home.get_row(rows.id(row));

    process_row(row);
    process_row(home_row);
}

export function toggle_collapse(message) {
    popovers.hide_all();
    if (message.is_me_message) {
        // Disabled temporarily because /me messages don't have a
        // styling for collapsing /me messages (they only recently
        // added multi-line support).  See also popovers.js.
        return;
    }

    // This function implements a multi-way toggle, to try to do what
    // the user wants for messages:
    //
    // * If the message is currently showing any [More] link, either
    //   because it was previously condensed or collapsed, fully display it.
    // * If the message is fully visible, either because it's too short to
    //   condense or because it's already uncondensed, collapse it

    const row = message_lists.current.get_row(message.id);
    if (!row) {
        return;
    }

    const content = row.find(".message_content");
    const is_condensable = content.hasClass("could-be-condensed");
    const is_condensed = content.hasClass("condensed");
    if (message.collapsed) {
        if (is_condensable) {
            message.condensed = true;
            content.addClass("condensed");
            show_message_expander(row);
            row.find(".message_condenser").hide();
        }
        uncollapse(row);
    } else {
        if (is_condensed) {
            message.condensed = false;
            content.removeClass("condensed");
            hide_message_expander(row);
            row.find(".message_condenser").show();
        } else {
            collapse(row);
        }
    }
}

export function clear_message_content_height_cache() {
    _message_content_height_cache.clear();
}

export function un_cache_message_content_height(message_id) {
    _message_content_height_cache.delete(message_id);
}

function get_message_height(elem, message_id) {
    if (_message_content_height_cache.has(message_id)) {
        return _message_content_height_cache.get(message_id);
    }

    // shown to be ~2.5x faster than Node.getBoundingClientRect().
    const height = elem.offsetHeight;
    if (!recent_topics_util.is_visible()) {
        _message_content_height_cache.set(message_id, height);
    }
    return height;
}

export function hide_message_expander(row) {
    if (row.find(".could-be-condensed").length !== 0) {
        row.find(".message_expander").hide();
    }
}

export function hide_message_condenser(row) {
    if (row.find(".could-be-condensed").length !== 0) {
        row.find(".message_condenser").hide();
    }
}

export function show_message_expander(row) {
    if (row.find(".could-be-condensed").length !== 0) {
        row.find(".message_expander").show();
    }
}

export function show_message_condenser(row) {
    if (row.find(".could-be-condensed").length !== 0) {
        row.find(".message_condenser").show();
    }
}

export function condense_and_collapse(elems) {
    const height_cutoff = message_viewport.height() * 0.65;
    const datestr_cutoff = getUnixTime(startOfToday());
    for (const elem of elems) {
        const content = $(elem).find(".message_content");

        if (content.length !== 1) {
            // We could have a "/me did this" message or something
            // else without a `message_content` div.
            continue;
        }

        const message_id = rows.id($(elem));

        if (!message_id) {
            continue;
        }

        const message = message_lists.current.get(message_id);
        if (message === undefined) {
            continue;
        }

        const message_height = get_message_height(elem, message.id);
        const long_message = message_height > height_cutoff;

        // ******* collapsed aka [+] button ********

        // Completely hide the message and replace it with a [+]
        // link if the user has collapsed it.
        // do this early, since it speeds up rendering
        if (message.collapsed && message.force_uncollapsed) {
//            console.log("fc: uncollapse (force): " + message.content.substr(0,40));
            fc_uncollapse($(elem), message, datestr_cutoff);
        } else
        if (message.collapsed && message.unread) {
//            console.log("fc: uncollapse (unread): " + message.content.substr(0,40));
            fc_uncollapse($(elem), message, datestr_cutoff);
        } else
        if (message.collapsed && long_message) {
//            console.log("fc: uncollapse (is_thoughtful): " + message.content.substr(0,40));
            fc_uncollapse($(elem), message, datestr_cutoff);
        } else
        if (message.collapsed || (!message.unread && !message.force_uncollapsed)) {
//            console.log("fc: collapsed: " + message.content.substr(0,40));
            fc_collapse($(elem), message, datestr_cutoff);
            content.addClass("collapsed");
            $(elem).find(".message_expander").show();
//        } else {
//            console.log("fc: uncollapse (default): " + message.content.substr(0,40));
        }

        // ******* condensed ********

        if (long_message) {
            content.addClass("could-be-condensed");
        } else {
            content.removeClass("could-be-condensed");
        }

        // If message.condensed is defined, then the user has manually
        // specified whether this message should be expanded or condensed.
        if (message.condensed === true) {
            condense_row($(elem));
            continue;
        }

        if (message.condensed === false) {
            uncondense_row($(elem));
            continue;
        }

        if (long_message) {
            condense_row($(elem));
        } else {
            uncondense_row($(elem));
        }
    }
}

export function initialize() {
    $("#message_feed_container").on("click", ".message_expander,.fc_message_expander,.fc_summary", function (e) {
        // Expanding a message can mean either uncollapsing or
        // uncondensing it.
        const row = $(this).closest(".message_row");
        const message = message_lists.current.get(rows.id(row));
        const content = row.find(".message_content");
        const is_fc = ($(this).hasClass("fc_message_expander") || $(this).hasClass("fc_summary"));
        if (message.collapsed || is_fc) {
            // Uncollapse.
            uncollapse(row);
        } else if (content.hasClass("condensed")) {
            // Uncondense (show the full long message).
            message.condensed = false;
            content.removeClass("condensed");
            $(this).hide();
            row.find(".message_condenser").show();
        }
        e.stopPropagation();
        e.preventDefault();
    });

    $("#message_feed_container").on("click", ".fc_message_collapser", function (e) {
        const row = $(this).closest(".message_row");
        collapse(row);
        e.stopPropagation();
        e.preventDefault();
    });

    $("#message_feed_container").on("click", ".message_condenser", function (e) {
        const row = $(this).closest(".message_row");
        message_lists.current.get(rows.id(row)).condensed = true;
        condense_row(row);
        e.stopPropagation();
        e.preventDefault();
    });
}
