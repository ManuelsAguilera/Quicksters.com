import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class JuegosService {
  private apiUrl = 'http://localhost:5000'; // Asegúrate que coincida con tu backend

  constructor(private http: HttpClient) {}

  importarDesdeSteam(appid: number) {
    return this.http.post(`${this.apiUrl}/db/juegos/steam/${appid}`, {});
  }

  obtenerJuegos() {
    return this.http.get<any>(`${this.apiUrl}/db/juegos`);
  }
}
