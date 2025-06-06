import { Component, OnInit } from '@angular/core';
import { IonicModule } from '@ionic/angular';
import { ComponentModule } from 'src/app/components/component.module';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-registro',
  templateUrl: './registro.page.html',
  styleUrls: ['./registro.page.scss'],
  standalone: true,
  imports: [IonicModule, ComponentModule, FormsModule]
})
export class RegistroPage implements OnInit {

  constructor() { }

  ngOnInit() {
  
  }

  onSubmit() {
    console.log("Formulario enviado");
  }
}

