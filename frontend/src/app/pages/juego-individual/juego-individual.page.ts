import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from 'src/app/service/api.service';
import { firstValueFrom } from 'rxjs';

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

  constructor(
    private route: ActivatedRoute,
    private api: ApiService
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
}