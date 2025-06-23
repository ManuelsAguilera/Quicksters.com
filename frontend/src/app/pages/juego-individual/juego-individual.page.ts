import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from 'src/app/service/api.service';

@Component({
  selector: 'app-juego-individual',
  templateUrl: './juego-individual.page.html',
  styleUrls: ['./juego-individual.page.scss'],
  standalone: false
})
export class JuegoIndividualPage implements OnInit {
  juego: any;
  categorias: any[] = [];

  constructor(private route: ActivatedRoute, private api: ApiService) {}

  ngOnInit() {
    const id = this.route.snapshot.paramMap.get('id');
    this.api.get(`/db/juegos/${id}/completo`).subscribe((resp: any) => {
      this.juego = resp.juego;
      this.categorias = resp.categorias;
    });
  }
}