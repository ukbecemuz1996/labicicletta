odoo.define("labicicletta.cart_limit", function (require) {
  "use strict";
  var publicWidget = require("web.public.widget");
  var Dialog = require("web.Dialog");

  publicWidget.registry.CartLimit = publicWidget.Widget.extend({
    selector: "#o_cart_summary",
    /**
     * @override
     */
    async start() {
      await this._super(...arguments);
      this._sniffCartLimit();
    },

    _sniffCartLimit() {
      const queryString = window.location.search;
      const urlParams = new URLSearchParams(queryString);
      if (urlParams.has("cart_limit") && urlParams.has("cart_limit_msg")) {
        const cart_limit = urlParams.get("cart_limit");
        const cart_limit_msg = urlParams.get("cart_limit_msg");
        if (cart_limit_msg === "exceeded") {
          urlParams.delete("cart_limit");
          urlParams.delete("cart_limit_msg");

          let msg = "";
          const langAttr = document.documentElement.lang;
          if (langAttr) {
            const attrArray = langAttr.split("-");
            const lang = attrArray[0];
            switch (lang) {
              case "en":
                msg = "Your total amount can`t be less than " + cart_limit;
                break;
              case "ar":
                msg = "لا يمكن للمجموع الكلي أن يكون أقل من " + cart_limit;
                break;
              default:
                msg = "Your total amount can`t be less than " + cart_limit;
                break;
            }
          } else {
            msg = "Your total amount can`t be less than " + cart_limit;
          }

          window.history.replaceState(
            {},
            "",
            `${window.location.pathname}?${urlParams}${window.location.hash}`
          );

          Dialog.alert(this, msg, {});
        }
      }
    },
  });

  publicWidget.registry.WorkingHours = publicWidget.Widget.extend({
    selector: "#wrapwrap",
    /**
     * @override
     */
    async start() {
      await this._super(...arguments);
      this._sniffWorkingHours();
    },

    _sniffWorkingHours() {
      const queryString = window.location.search;
      const urlParams = new URLSearchParams(queryString);
      if (urlParams.has("working_hours")) {
        const working_hours = urlParams.get("working_hours");
        if (working_hours === "outside") {
          urlParams.delete("working_hours");

          let msg = "";
          const langAttr = document.documentElement.lang;
          if (langAttr) {
            const attrArray = langAttr.split("-");
            const lang = attrArray[0];
            switch (lang) {
              case "en":
                msg =
                  "We are now outside of service because we are now outside of our working hours";
                break;
              case "ar":
                msg =
                  "نحن الآن خارج نطاق الخدمة لأننا الآن خارح نطاق ساعات العمل";
                break;
              default:
                msg =
                  "We are now outside of service because we are now outside of our working hours";
                break;
            }
          } else {
            msg =
              "We are now outside of service because we are now outside of our working hours";
          }

          window.history.replaceState(
            {},
            "",
            `${window.location.pathname}?${urlParams}${window.location.hash}`
          );

          Dialog.alert(this, msg, {});
        }
      }
    },
  });
});
