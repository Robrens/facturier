$(document).ready(function () {


    var array = []
    $('.pre-total').each(function () {
        array.push($(this).text());
    })
    var total = 0;
    for (let i = 0; i < array.length; i++) {
        var calc = parseInt(array[i]);
        total += calc;
    }
    $('.total').text(total);

    $.fn.editable.defaults.mode = 'inline';
    $('.status').editable({
        value: 2,
        source: [{
                value: 'paid',
                text: 'paid'
            },
            {
                value: 'in-progress',
                text: 'in-progress'
            },
            {
                value: 'reflate',
                text: 'reflate'
            },
        ]
    });
    $('.is_bill').editable({
        value: 2,
        source: [{
                value: 'False',
                text: 'Quotation'
            },
            {
                value: 'True',
                text: 'Bill'
            }
        ]
    })
    $('.ref').editable({});
    $('.product-name').editable({});



});