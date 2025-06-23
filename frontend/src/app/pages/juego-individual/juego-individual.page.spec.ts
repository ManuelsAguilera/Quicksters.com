import { ComponentFixture, TestBed } from '@angular/core/testing';
import { JuegoIndividualPage } from './juego-individual.page';

describe('JuegoIndividualPage', () => {
  let component: JuegoIndividualPage;
  let fixture: ComponentFixture<JuegoIndividualPage>;

  beforeEach(() => {
    fixture = TestBed.createComponent(JuegoIndividualPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
