import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from 'src/app/service/api.service';
import { firstValueFrom } from 'rxjs';
import { ToastController } from '@ionic/angular';

@Component({
  selector: 'app-juego-individual',
  templateUrl: './juego-individual.page.html',
  styleUrls: ['./juego-individual.page.scss'],
  standalone: false
})
export class JuegoIndividualPage implements OnInit {
  juego: any = {};
  categorias: any[] = [];
  speedruns: any[] = [];
  categoriaSeleccionada: string | null = null;
  formSpeedrun = {
    idcategoria: null,
    duracion: '',
    url_video: ''
  };

  constructor(
    private route: ActivatedRoute,
    private api: ApiService,
    private toastController: ToastController
  ) {}

  async ngOnInit() {
    const id = this.route.snapshot.paramMap.get('id');
    if (id) {
      await this.cargarJuegoCompleto(+id);
    }
  }

  async cargarJuegoCompleto(idJuego: number) {
    try {
      const resp: any = await firstValueFrom(this.api.get(`/db/juegos/${idJuego}/completo`));
      this.juego = resp.juego;
      this.categorias = resp.categorias;

      if (this.categorias.length > 0) {
        this.categoriaSeleccionada = this.categorias[0].idCategoria.toString();
        await this.cargarSpeedruns(Number(this.categoriaSeleccionada));
      }
    } catch (error) {
      console.error('Error al cargar datos del juego:', error);
    }
  }

  async cambiarCategoria(idCategoriaStr: string | undefined) {
    if (!idCategoriaStr) return;
    const idCategoria = Number(idCategoriaStr);
    if (!isNaN(idCategoria)) {
      this.categoriaSeleccionada = idCategoriaStr;
      await this.cargarSpeedruns(idCategoria);
    }
  }

  async cargarSpeedruns(idCategoria: number) {
    try {
      const runs: any = await firstValueFrom(
        this.api.get(`/db/speedruns/juego/${this.juego.idjuego}/categoria/${idCategoria}`)
      );
      this.speedruns = runs;
    } catch (error) {
      console.error('Error al cargar speedruns:', error);
    }
  }

  async subirSpeedrun() {
    const token = localStorage.getItem('token');
    
    if (!token) {
      this.mostrarToast('Debes iniciar sesión para subir una speedrun.', 'danger');
      return;
    }

    const payload = {
      idcategoria: this.formSpeedrun.idcategoria,
      duracion: this.formSpeedrun.duracion,
      url_video: this.formSpeedrun.url_video,
      idjuego: this.juego.idjuego
    };
  
    try {
      await firstValueFrom(
        this.api.post('/db/speedruns', payload, {
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
          }
        })
      );
  
      this.formSpeedrun = { idcategoria: null, duracion: '', url_video: '' };
      
      if (this.categoriaSeleccionada) {
        await this.cargarSpeedruns(Number(this.categoriaSeleccionada));
      }
      this.mostrarToast('Speedrun subida exitosamente.', 'success');
    } catch (error) {
      console.error('Error al subir speedrun:', error);
      this.mostrarToast('Hubo un error al subir la speedrun.', 'danger');
    }
  }

  async mostrarToast(mensaje: string, color: 'success' | 'danger') {
    const toast = await this.toastController.create({
      message: mensaje,
      duration: 3000,
      position: 'top',
      color: color
    });
    toast.present();
  }

}