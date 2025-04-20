import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { JuegosPageRoutingModule } from './juegos-routing.module';
import {ComponentModule} from '../../components/component.module';
import { JuegosPage } from './juegos.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    ComponentModule,
    JuegosPageRoutingModule
  ],
  declarations: [JuegosPage]
})
export class JuegosPageModule {}
