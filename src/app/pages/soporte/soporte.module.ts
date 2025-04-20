import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { IonicModule } from '@ionic/angular';
import { SoportePageRoutingModule } from './soporte-routing.module';
import { SoportePage } from './soporte.page';
import { ComponentModule } from '../../components/component.module';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    SoportePageRoutingModule,
    ComponentModule  // Añade este módulo
  ],
  declarations: [SoportePage]
})
export class SoportePageModule {}