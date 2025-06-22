import { Component, OnInit } from '@angular/core';
import { JuegosService } from '../../service/juegos.service';

@Component({
  selector: 'app-juegos',
  templateUrl: './juegos.page.html',
  styleUrls: ['./juegos.page.scss'],
  standalone: false,
})
export class JuegosPage implements OnInit {
  juegos: any[] = [];
  nuevoAppid: number = 0;
  cantidadJuegos = 24;
  
  constructor(private juegosService: JuegosService) {}

  ngOnInit() {
    this.cargarJuegos();
  }

  cargarJuegos() {
    this.juegosService.obtenerJuegos().subscribe((resp: any) => {
      this.juegos = resp.data;
      this.cantidadJuegos = this.juegos.length;
    });
  }

  importarJuego() {
    if (this.nuevoAppid > 0) {
      this.juegosService.importarDesdeSteam(this.nuevoAppid).subscribe({
        next: (resp: any) => {
          this.cargarJuegos();
          this.nuevoAppid = 0;
        },
        error: (err: any) => {
          console.error(err);
          alert('Error al importar el juego');
        }
      });
    }
  }
  aumentarJuegos() {
    this.cantidadJuegos += 12; // Aumentar de 12 en 12
  }
  
  resetearJuegos() {
    this.cantidadJuegos = 8; // Volver al valor inicial
  }
}





// export class JuegosPage implements OnInit {
//   juegos: any[] = [];
//   nuevoAppid: number = 0;

//   constructor(private juegosService: JuegosService) {}

//   ngOnInit() {
//     this.cargarJuegos();
//   }

//   cargarJuegos() {
//     this.juegosService.obtenerJuegos().subscribe(resp => {
//       this.juegos = resp.data;
//     });
//   }

//   importarJuego() {
//     if (this.nuevoAppid > 0) {
//       this.juegosService.importarDesdeSteam(this.nuevoAppid).subscribe({
//         next: (resp) => {
//           this.cargarJuegos();
//           this.nuevoAppid = 0;
//         },
//         error: (err) => {
//           console.error(err);
//           alert('Error al importar el juego');
//         }
//       });
//     }
//   }
// }


// export class JuegosPage implements OnInit {

//   cantidadJuegos = 20;

//   constructor() { }

//   ngOnInit() {
//   }

//   aumentarJuegos() {
//     this.cantidadJuegos += 5; // Aumentar de 4 en 4
//   }
  
//   resetearJuegos() {
//     this.cantidadJuegos = 8; // Volver al valor inicial
//   }
// }
