import { Component, OnInit, ViewChild } from '@angular/core';
import { IonicModule } from '@ionic/angular';
import { ComponentModule } from 'src/app/components/component.module';
import { FormsModule,NgForm } from '@angular/forms';
import { ApiService } from 'src/app/service/api.service';
import { Router } from '@angular/router';
import { ToastController } from '@ionic/angular';

@Component({
  selector: 'app-registro',
  templateUrl: './registro.page.html',
  styleUrls: ['./registro.page.scss'],
  standalone: true,
  imports: [IonicModule, ComponentModule, FormsModule]
})
export class RegistroPage implements OnInit {


  private async mostrarMensaje(mensaje: string) {
  const toast = await this.toastController.create({
    message: mensaje,
    duration: 2000,
    position: 'bottom'
  });
  await toast.present();
  }

  registroData = {
    username: '',
    correo: '',
    nacionalidad: '',
    contraseña: ''
  };
  confPassword = '';
  password = '';


  constructor(
    private apiService: ApiService,
    private router: Router,
    private toastController: ToastController
  ) { }

  ngOnInit() { }

  async onSubmit() {
    if (this.confPassword !== this.confPassword) {
      await this.mostrarMensaje('Las contraseñas no coinciden');
      return;
    }

    this.registroData.contraseña = this.confPassword;

    if (!this.registroData.username || 
    !this.registroData.correo || 
    !this.registroData.nacionalidad || 
    !this.registroData.contraseña) {
    this.mostrarMensaje('Por favor, completa todos los campos');
    console.log('Campos estan vacios:', this.registroData);
    return;
  }
    

    this.apiService.register(
      this.registroData.username,
      this.registroData.correo,
      this.registroData.nacionalidad,
      this.registroData.contraseña
    ).subscribe({
      next: async (response) => {
        await this.mostrarMensaje('Registro exitoso');
        this.router.navigate(['/login']);
        console.log('Registro')
      },
      error: async (error) => {
        console.log(this.registroData);
        await this.mostrarMensaje(error.error.msg || 'Error en el registro, confirma los datos ingresados');
      }
    });
  }


}