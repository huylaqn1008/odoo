/** @odoo-module **/
import { Card } from "./components/card/card";
import { Component, useState } from "@odoo/owl";
export class Main extends Component {
    setup() {
        this.state = useState({});
    }
    static template = "tutorial_theme.main";
    static components = { Card };
}