/** @odoo-module **/

import { Component } from "@odoo/owl";

export class LoadingOverlay extends Component {
    static template = "sm_loading_animation.LoadingOverlay";
    static props = {
        visible: { type: Boolean, optional: true },
    };
}
