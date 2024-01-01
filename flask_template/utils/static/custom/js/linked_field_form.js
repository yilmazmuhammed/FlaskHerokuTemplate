function do_action_of_linked_fields(list_field, str_field) {
  let value = list_field.val();
  if (value === "new") {
    str_field.val("");
    str_field.closest(".form-group").show();
  } else {
    str_field.val(value);
    str_field.closest(".form-group").hide();
  }
}

function connect_fields(list_field, str_field) {
  // Liste değeri her değiştiğinde seçilen değere göre işlem yap
  list_field.change(function () {
    do_action_of_linked_fields(list_field, str_field);
  });

  // Sayfa açılışındaki değere göre işlem yap
  do_action_of_linked_fields(list_field, str_field);

  // <divider> geçen seçenekleri pasif ap
  $("option").filter(function () {
    return $(this).text() === "<divider>";
  }).attr("disabled", "").text("-----------");
}

/* Kullanım:
    <script>
      $(document)
        .ready(function() {
          connect_fields($("[name='sub_type_list']"), $("[name='sub_type']"));
        });
    </script>
 */