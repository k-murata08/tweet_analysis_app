$('#csv_table').after(
    '<button type="button" id="download_csv_btn" class="btn btn-primary">CSV Download</button>'
);

$('#download_csv_btn').click(function() {
    var filename = $("#csv_table").attr("data-name") + ".csv";
    $("#csv_table").table2csv('output', { appendTo: '#out' });
    $("#csv_table").table2csv('output', { filename:  filename });
    $("#csv_table").table2csv();
});

// tr全体をリンクにする
$('tbody tr[data-href]').addClass('clickable').click( function() {
    window.location = $(this).attr('data-href');
}).find('a').hover( function() {
    $(this).parents('tr').unbind('click');
}, function() {
    $(this).parents('tr').click( function() {
        window.location = $(this).attr('data-href');
    });
});