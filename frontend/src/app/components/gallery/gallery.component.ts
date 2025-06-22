import { Component, OnInit,OnChanges,SimpleChanges,Input } from '@angular/core';

interface GalleryImage {
  src: string;
  alt: string;
  title: string;
}


@Component({
  selector: 'app-gallery',
  templateUrl: './gallery.component.html',
  styleUrls: ['./gallery.component.scss'],
  standalone:false,
})
export class GalleryComponent  implements OnInit {
  //
   @Input() cantImages: number= 12;
   @Input() title:string= "no"
   @Input() juegos: any[] = [];
   
  currentCantImages:number;

  images: GalleryImage[];

  
  constructor() {
    this.currentCantImages = this.cantImages;
    this.images = this.createImagesList();
  }

  ngOnChanges(changes:SimpleChanges) {
    if (changes['cantImages']) {
      if (changes['cantImages'].currentValue > this.currentCantImages) {
        this.addImagesList();
      } else if (changes['cantImages'].currentValue < this.currentCantImages) {
        this.images = this.images.slice(0, changes['cantImages'].currentValue);
      }
      
      this.currentCantImages = changes['cantImages'].currentValue;
    }
  }

  ngOnInit() {
    this.currentCantImages = this.cantImages;
  }

  private createImagesList():GalleryImage[]
  {
    let imageList:GalleryImage[]= []
    for (let i = 0; i < this.cantImages; i++)
    {
      //Crear una imagen nueva y hacer append a nuestra lista
      imageList.push({
        src: `assets/shapes.svg`,  // Ciclo entre 5 imágenes de juegos
        alt: `Juego ${i} screenshot`,
        title: `Juego ${i}`
      });

    }
    return imageList;
  }

  private addImagesList()
  {
    for (let i = this.currentCantImages; i < this.cantImages; i++)
      {
        //Crear una imagen nueva y hacer append a nuestra lista
        this.images.push({
          src: `assets/shapes.svg`,  // Ciclo entre 5 imágenes de juegos
          alt: `Juego ${i} screenshot`,
          title: `Juego ${i}`
        });
  
      }
  }



}
