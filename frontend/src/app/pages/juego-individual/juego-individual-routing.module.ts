import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { JuegoIndividualPage } from './juego-individual.page';

const routes: Routes = [
  {
    path: '',
    component: JuegoIndividualPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class JuegoIndividualPageRoutingModule {}
