import { Component, OnInit } from '@angular/core';
import { IonicModule } from '@ionic/angular';
import { ComponentModule } from 'src/app/components/component.module';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ApiService } from 'src/app/service/api.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.page.html',
  styleUrls: ['./login.page.scss'],
  standalone: false,
})
export class LoginPage implements OnInit {
  loginForm!: FormGroup;

  constructor(
    private formBuilder: FormBuilder, 
    private apiService: ApiService
  ) {}

  ngOnInit() {
    this.loginForm = this.formBuilder.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(6)]]
    });
  }

  get email() { 
    return this.loginForm.get('email'); 
  }
  
  get password() { 
    return this.loginForm.get('password'); 
  }

  onSubmit() {
    if (this.loginForm.valid) {
      const { email, password } = this.loginForm.value;
      console.log('Login attempt:', { email, password });
      this.apiService.login(email, password).subscribe(
        response => {
          console.log('Login successful:', response);
          // Aquí puedes redirigir al usuario a otra página o mostrar un mensaje de éxito
        },
        error => {
          console.error('Login failed:', error);
          // Aquí puedes manejar el error, por ejemplo, mostrando un mensaje al usuario
        }
      );
      
    } else {
      this.markFormGroupTouched(this.loginForm);
    }
    //Test api
    this.apiService.testConnection().subscribe(
        response => {
          console.log('API Test Response:', response);
        },
        error => {
          console.error('API Test Error:', error);
        }
      )
  }

  private markFormGroupTouched(formGroup: FormGroup) {
    Object.values(formGroup.controls).forEach(control => {
      control.markAsTouched();

      if (control instanceof FormGroup) {
        this.markFormGroupTouched(control);
      }
    });
  }
}