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
   @Input() rows: number = 2;
   @Input() images: GalleryImage[] = [
    { src: 'assets/shapes.svg', alt: 'Imagen 1', title: 'Juegos 1' },
    { src: 'assets/shapes.svg', alt: 'Imagen 2', title: 'Juegos 2' },
    { src: 'assets/shapes.svg', alt: 'Imagen 3', title: 'Juegos 3' },
    { src: 'assets/shapes.svg', alt: 'Imagen 4', title: 'Juegos 4' },
    { src: 'assets/shapes.svg', alt: 'Imagen 5', title: 'Juegos 5' },
    { src: 'assets/shapes.svg', alt: 'Imagen 6', title: 'Juegos 6' },
    { src: 'assets/shapes.svg', alt: 'Imagen 7', title: 'Juegos 7' },
    { src: 'assets/shapes.svg', alt: 'Imagen 8', title: 'Juegos 8' },
    { src: 'assets/shapes.svg', alt: 'Imagen 9', title: 'Juegos 9' },
    { src: 'assets/shapes.svg', alt: 'Imagen 10', title: 'Juegos 10' },
    { src: 'assets/shapes.svg', alt: 'Imagen 11', title: 'Juegos 11' },
    { src: 'assets/shapes.svg', alt: 'Imagen 12', title: 'Juegos 12' },
  ];

  //Lo que mostraremos de las imagenes
  imagesGrouped: GalleryImage[][] = [];

   
  constructor() { }

  ngChanges() {
    this.groupImages();
  }

  ngOnInit() {
    this.groupImages();
  }

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
  }



}
