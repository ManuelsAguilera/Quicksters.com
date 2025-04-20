import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {IonicModule} from '@ionic/angular'; 
import {RouterModule} from '@angular/router';

import { HeaderComponent } from '../components/header/header.component';
import { CarouselComponent } from '../components/carousel/carousel.component';
import { GalleryComponent } from '../components/gallery/gallery.component';
import { FooterComponent } from './footer/footer.component';

@NgModule({

  declarations: [HeaderComponent,CarouselComponent,GalleryComponent,FooterComponent], // Declara el componente
  imports: [CommonModule,IonicModule,RouterModule], // Importa CommonModule para usar directivas básicas de Angular
  exports: [HeaderComponent,CarouselComponent,GalleryComponent,FooterComponent] // Exporta el componente para que otros módulos puedan usarlo
})
export class ComponentModule {}