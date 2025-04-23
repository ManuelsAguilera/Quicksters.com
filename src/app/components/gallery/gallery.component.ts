import { Component, OnInit,OnChanges,Input } from '@angular/core';

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
   
  images: GalleryImage[] = this.createImagesList();

  //Lo que mostraremos de las imagenes
  imagesGrouped: GalleryImage[][] = [];

   
  constructor() {
  }

  ngChanges() {
    //this.groupImages();
  }

  ngOnInit() {
    //this.groupImages();
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
 /*
  private groupImages()
  {
    // Dividir las imágenes en filas
    const totalImages = this.images.length;
    const imagesPerRow = Math.ceil(totalImages / this.rows);
    
    this.imagesGrouped = [];
    // Crear las filas
    for (let i = 0; i < this.rows; i++) {
      const startIndex = i * imagesPerRow;
      const endIndex = Math.min(startIndex + imagesPerRow, totalImages);
      this.imagesGrouped.push(this.images.slice(startIndex, endIndex));
    }
  }*/



}
