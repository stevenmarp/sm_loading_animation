/** @odoo-module **/

import { LoadingIndicator } from "@web/webclient/loading_indicator/loading_indicator";
import { patch } from "@web/core/utils/patch";
import { useState, onWillStart } from "@odoo/owl";
import { registry } from "@web/core/registry";

patch(LoadingIndicator.prototype, {
    setup() {
        super.setup(...arguments);
        this.config = useState({
            type: 'spinner_1',
            position: 'bottom-right',
            color: '#714B67',
            bgColor: '#FFFFFF',
            showText: true,
            text: 'Loading...',
            fullscreen: false,
            showLogo: false,
        });

        onWillStart(async () => {
            try {
                const params = await this.env.services.orm.call(
                    'ir.config_parameter',
                    'get_param',
                    ['snk_loading_animation.animation_type', 'spinner_1']
                );
                this.config.type = params || 'spinner_1';
                
                this.config.position = await this.env.services.orm.call(
                    'ir.config_parameter', 'get_param',
                    ['snk_loading_animation.position', 'bottom-right']
                ) || 'bottom-right';
                
                this.config.color = await this.env.services.orm.call(
                    'ir.config_parameter', 'get_param',
                    ['snk_loading_animation.color', '#714B67']
                ) || '#714B67';
                
                this.config.bgColor = await this.env.services.orm.call(
                    'ir.config_parameter', 'get_param',
                    ['snk_loading_animation.bg_color', '#FFFFFF']
                ) || '#FFFFFF';
                
                this.config.showText = await this.env.services.orm.call(
                    'ir.config_parameter', 'get_param',
                    ['snk_loading_animation.show_text', 'True']
                ) !== 'False';
                
                this.config.text = await this.env.services.orm.call(
                    'ir.config_parameter', 'get_param',
                    ['snk_loading_animation.text', 'Loading...']
                ) || 'Loading...';
            } catch (e) {
                console.log('Loading animation config not loaded, using defaults');
            }
        });
    },
    
    get positionClass() {
        return `snk-position-${this.config.position}`;
    },
    
    get animationClass() {
        return `snk-animation-${this.config.type}`;
    },
});

patch(LoadingIndicator, {
    template: "snk_loading_animation.LoadingIndicator",
});
