// Read book
    function readBookModalForm() {
      document.addEventListener('DOMContentLoaded', (e) => {
        var readButtons = document.getElementsByClassName("read-book");
        for (var index=0; index < readButtons.length; index++) {
          modalForm(readButtons[index], {formURL: readButtons[index]["dataset"]["formUrl"]});
        }
      });
    };
   readBookModalForm();


   function Mmm() {
        var readButtons = document.getElementsByClassName("read-book");
        for (var index=0; index < readButtons.length; index++) {
          modalForm(readButtons[index], {formURL: readButtons[index]["dataset"]["formUrl"]});
        }

    };
