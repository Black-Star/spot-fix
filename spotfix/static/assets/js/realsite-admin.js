$(document).ready(function() {
    'use strict';

    /**
    * Input file
    */
    $('#input-file').fileinput({
        initialPreview: [
        "<img src='assets/img/tmp/medium/1.jpg' class='file-preview-image' alt='The Moon' title='Property 1'>",
        "<img src='assets/img/tmp/medium/2.jpg' class='file-preview-image' alt='The Earth' title='Property 2'>",
        ],
        overwriteInitial: true,
        initialCaption: "Your Uploaded Properties"
    });

    /**
     * Bootstrap select
     */
    $('select').selectpicker({
        size: 10
    });

    /**
     * Input Group
     */
    $('.input-group .form-control').on('focus', function() {
        $(this).closest('.input-group').find('.input-group-addon').addClass('active');
    }).on('blur', function() {
        $(this).closest('.input-group').find('.input-group-addon').removeClass('active');
    });

    /**
     * Map
     */


    /**
     * Login
     */
    $('.admin-sidebar-secondary button').click(function(e) {
        e.preventDefault();

        $('body').addClass('open');

        $('.admin-sidebar-secondary').animate({
            'display': 'none'
        }, 1250, function() {
            $('.admin-sidebar-secondary').css('display', 'none');
            createChart();
        });
    });

    if ($('body').hasClass('hide-secondary-sidebar')) {
        createChart();
    }

    function createChart() {
        nv.addGraph(function() {
            var chart = nv.models.multiBarChart()
            .transitionDuration(350)
            .reduceXTicks(true)   //If 'false', every single x-axis tick label will be rendered.
            .rotateLabels(0)      //Angle to rotate x-axis labels.
            .showControls(true)   //Allow user to switch between 'Grouped' and 'Stacked' mode.
            .groupSpacing(0.1)    //Distance between each group of bars.
            ;

            chart.xAxis
            .tickFormat(d3.format(',f'));

            chart.yAxis
            .tickFormat(d3.format(',.1f'));

            d3.select('#chart svg')
            .datum(exampleData())
            .call(chart);

            nv.utils.windowResize(chart.update);

            return chart;
        });

        //Generate some nice data.
        function exampleData() {
            return stream_layers(2,10+Math.random()*100,.1).map(function(data, i) {
                return {
                    key: 'Stream #' + i,
                    values: data
                };
            });
        }
    }
});
