import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {IonicModule} from '@ionic/angular'; 
import { HeaderComponent } from '../components/header/header.component';

@NgModule({
  declarations: [HeaderComponent], // Declara el componente
  imports: [CommonModule,IonicModule], // Importa CommonModule para usar directivas básicas de Angular
  exports: [HeaderComponent] // Exporta el componente para que otros módulos puedan usarlo
})
export class ComponentModule {}