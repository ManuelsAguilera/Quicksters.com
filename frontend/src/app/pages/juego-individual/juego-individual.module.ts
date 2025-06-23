import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { JuegoIndividualPageRoutingModule } from './juego-individual-routing.module';
import { ComponentModule } from '../../components/component.module';
import { JuegoIndividualPage } from './juego-individual.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    JuegoIndividualPageRoutingModule,
    ComponentModule,
  ],
  declarations: [JuegoIndividualPage]
})
export class JuegoIndividualPageModule {}
