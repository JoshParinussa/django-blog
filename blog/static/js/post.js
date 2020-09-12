"use strict";

var Inbox = function() {

    var initPost = function() {
        var deleted_selected = [];
        $('#post-list-container').on('click', '#btn-load', function(e) {
            e.preventDefault();
            var dis = $(this);
            var next_page = dis.data('next-page')
            var category_val = $('#category').val()
            var search_box_val = $('#search-post').val()
            searchResult(search_box_val, category_val, next_page);
        });

        $('#search-post').on('input', function(e) {
            var input = $(this);
            var val = input.val();
            var category_val = $('#category').val()
            searchResult(val, category_val);
        });

        $('#category').on('change', function(e) {
            var input = $(this);
            var val = input.val();
            var search_box_val = $('#search-post').val()

            searchResult(search_box_val, val)
        });

        var searchResult = function(searchBox, category, page = '') {
            var query_string = ''
            var currLoc = $(location).attr('href');
            if (searchBox != '') {
                if (query_string != '') {
                    query_string = query_string + '&q=' + searchBox
                } else {
                    query_string = query_string + '?q=' + searchBox
                }
            }
            if (category != '') {
                if (query_string != '') {
                    query_string = query_string + '&c=' + category
                } else {
                    query_string = query_string + '?c=' + category
                }
            }
            if (page != '') {
                if (query_string != '') {
                    query_string = query_string + '&page=' + page
                } else {
                    query_string = query_string + '?page=' + page
                }
            }
            console.log(currLoc + query_string);
            $.get(currLoc + query_string, function(data) {
                if (page == '') {
                    $('#post-container').empty();
                }
                var $data = $(data);
                $data.find('.post-item').appendTo('#post-container');
                $('.inbox-button-load').empty();
                $data.find('#btn-load').appendTo('.inbox-button-load')
            });
        }

    }
    return {
        init: function() {
            initPost();
        }
    };
}();

jQuery(document).ready(function() {
    Inbox.init();
});