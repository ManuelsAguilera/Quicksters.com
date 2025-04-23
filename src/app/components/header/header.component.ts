import { Component, OnInit } from '@angular/core';
import {MenuController} from '@ionic/angular'

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss'],
  standalone: false
})
export class HeaderComponent  implements OnInit {

  constructor(private menuCtrl: MenuController) { }
  
  ngOnInit() {}

  openMenu() {
    console.log("XDD");
    this.menuCtrl.open('first');
  }

  closeMenu() {
    this.menuCtrl.close('first');
  }
}
