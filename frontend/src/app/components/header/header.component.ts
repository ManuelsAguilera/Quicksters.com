import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/service/api.service';
import { Observable } from 'rxjs';

import {MenuController} from '@ionic/angular'

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss'],
  standalone: false
})
export class HeaderComponent  implements OnInit {

  isAuthenticated$: Observable<boolean>;


  constructor(private menuCtrl: MenuController,private apiService: ApiService) {
    this.isAuthenticated$ = this.apiService.isAuthenticated$;
   }
  




  ngOnInit() {
    const token = localStorage.getItem('token');
    if (!token) {
      this.apiService.logout(); // This will set authState to false
    }

  }

  openMenu() {
    this.menuCtrl.open('first');
  }

  closeMenu() {
    this.menuCtrl.close('first');
  }


  logout() {
    this.apiService.logout();
    this.closeMenu();
  }

}
