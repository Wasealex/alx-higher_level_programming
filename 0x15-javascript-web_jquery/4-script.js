$('#toggle_header').click(function () {
  const header = $('header');
  const clss = header.attr('class');
  header.addClass(clss === 'red' ? 'green' : 'red');
  header.removeClass(clss === 'red' ? 'red' : 'green');
});
