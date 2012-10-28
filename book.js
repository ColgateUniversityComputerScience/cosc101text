/*
 * jsommers@colgate.edu 
 * javascript for think python book.
 */

/* "use strict"; */

var thinkbook = {
    start: function () {
        /* append some content to the header */
        jQuery("#header").append("<p>Reader take note: this book uses a bit of javascript to selectively hide chapters and handle other display tricks.  If you have trouble viewing it, you should either get a new browser (firefox or chrome are good choices), or try using a different book format like pdf or epub.  <p id='credlink'><a href=\"#\">Credits.</a></p>");

        // hide/show credit section
        jQuery("#credits").hide();
        jQuery("#credits").click(function() {
            jQuery("#credits").toggle();
        });

        jQuery("#credlink").click(function() {
            jQuery("#credits").toggle();
        });

        jQuery("#TOC").before("<div id='TOChead'></div>");
        jQuery("#TOChead").html("<h2 id=\"tocheader\">Table of contents</h2><h4 id=\"expandall\" class=\"toctoggler\">Expand all chapters</h4><h4 id=\"contractall\" class=\"toctoggler\">Hide all chapters</h4>");

        /* to every div following the #TOC id, add the chapterdiv class */
        jQuery("#TOC ~ div").addClass("chapterdiv");

        /* set up every chapter title h1 to be clickable */
        jQuery(".chapterdiv > h1").addClass("toggler");
        jQuery(".chapterdiv > h1").after("<h4 class=\"printlink\">Printable version</h4>");
        jQuery(".chapterdiv").map(function() {
             jQuery(this).children().not(".toggler").wrapAll("<div class=\"hideable\">");
        });

        jQuery(".toggler").click(function() {
            /* 
             * select next sibling element with class 'hideable' 
             * and toggle visibility on that element.
             */
            jQuery(this).next().slideToggle();
        });

        /* hide all chapter contents initially */
        jQuery(".hideable").slideUp();

        jQuery('span[class^="header-section-number"]').unwrap(); 

        /* fixme: footnotes */
        jQuery(".footnotes").hide();

        jQuery("body > div").not("#TOC").wrapAll("<div id=\"maincontent\">");
        jQuery("#maincontent").after("<div id=\"printblock\"></div>");

        /* fix up TOC to be mostly hidden and title-clickable */
        jQuery("#TOC").wrapInner("<div class=\"hideable\">");

        jQuery("#expandall").click(function() {
            jQuery(".hideable").slideDown();
        });

        jQuery("#contractall").click(function() {
            jQuery(".hideable").not("#TOC > div").slideUp();
        });

        /* handle printable link; clone the div, add it to
           a hidden printview div and only show that printview */
        jQuery(".printlink").click(function() {
            var p = jQuery(this).parent().parent().clone();
            jQuery("#maincontent").hide();
            jQuery("#TOC").hide()
            jQuery("#printblock").html(p);
            jQuery("#printblock").show();
            jQuery("#printblock .printlink").html("Return to normal view");

            /* reverse the changes we made before; clean up the
               printview div, and redisplay our original maincontent */
            jQuery("#printblock .printlink").click(function() {
                jQuery("#maincontent").show();
                jQuery("#TOC").show()
                jQuery("#printblock").hide();
                jQuery("#printblock").html("");
            });
        });

        jQuery("#TOC a").click(function() {
            var child = jQuery(this.hash).children(".hideable");
            if (child.length > 0) {
                child.slideDown();
            } else {
                var parent = jQuery(this.hash).parent(".hideable");
                parent.slideDown();
            }
        });    

        /* if page got opened with internal #anchor, go to it. */
        if (document.location.hash) {
            var lochash = document.location.hash;
            jQuery(lochash).parents().filter('.hideable').slideDown();
        }
    }
};

jQuery(thinkbook.start);
