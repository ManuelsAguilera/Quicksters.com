import { Component, OnInit,Input } from '@angular/core';
import { getElement } from 'ionicons/dist/types/stencil-public-runtime';

@Component({
  selector: 'app-foro-title',
  templateUrl: './foro-title.component.html',
  styleUrls: ['./foro-title.component.scss'],
  standalone:false,
})
export class ForoTitleComponent  implements OnInit {

  @Input() type: string = '';
  @Input() title:string = '';
  @Input() description:string='';
  @Input() postId:string="";
  @Input() color:string = '';

  typesOfTitle:string[] = ["section-title","forum-title","page-title"];

  
  constructor() { }

  ngOnInit() {}

  getPostThreads() : string
  {
    let cant = Math.floor(Math.random() * 800) + 1;

    return cant.toString();
  }

  getPostMessages() : string
  {
    let cant = Math.floor(Math.random() * 500) + 1;

    return cant.toString();
  }

  getLastPostName():string{
    return "Titulo ultimo post";
  }

  getLastPostProfilePicture():string
  {
    let rand = Math.floor(Math.random() * 3) + 1;

    switch(rand) {
      case 1: return "assets/profiles/cartoon.png";
      case 2: return "assets/profiles/anime.png";
      default: return "assets/quickster-support-320.png";
  }
}
  getColorClass(): string {
    if (this.type !== 'forum-title') return '';
    
    switch(this.color) {
      case 'light': return 'light-bg';
      case 'dark': return 'dark-bg';
      
      default: return 'dark-bg'; // Color por defecto
    }
  }
}
