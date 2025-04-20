import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {IonicModule} from '@ionic/angular'; 
import { HeaderComponent } from '../components/header/header.component';
import { CarouselComponent } from '../components/carousel/carousel.component';
import { GalleryComponent } from '../components/gallery/gallery.component';

@NgModule({
  declarations: [HeaderComponent,CarouselComponent,GalleryComponent], // Declara el componente
  imports: [CommonModule,IonicModule], // Importa CommonModule para usar directivas básicas de Angular
  exports: [HeaderComponent,CarouselComponent,GalleryComponent] // Exporta el componente para que otros módulos puedan usarlo
})
export class ComponentModule {}