import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { RegistroPageRoutingModule } from './registro-routing.module';
import { ComponentModule } from '../../components/component.module';
import { RegistroPage } from './registro.page';


@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    ComponentModule,
    RegistroPageRoutingModule,
    RegistroPage
  ],
})
export class RegistroPageModule {}
