import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ForosPage } from './foros.page';

const routes: Routes = [
  {
    path: '',
    component: ForosPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class ForosPageRoutingModule {}
