import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { RegistroPage } from './registro.page';

const routes: Routes = [
  {
    path: '',
    component: RegistroPage
  }
];

@NgModule({
  imports:[RouterModule.forChild(routes)],
  exports:[RouterModule],
})

export class RegistroPageRoutingModule {}
/*
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { JuegosPage } from './juegos.page';

const routes: Routes = [
  {
    path: '',
    component: JuegosPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class JuegosPageRoutingModule {}

*/
