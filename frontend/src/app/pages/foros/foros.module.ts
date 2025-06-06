import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { ForosPageRoutingModule } from './foros-routing.module';
import { ComponentModule } from '../../components/component.module'; 
import { ForosPage } from './foros.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    ComponentModule,
    ForosPageRoutingModule
  ],
  declarations: [ForosPage]
})
export class ForosPageModule {}
