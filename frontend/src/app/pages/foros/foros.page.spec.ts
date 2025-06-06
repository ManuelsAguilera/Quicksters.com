import { ComponentFixture, TestBed } from '@angular/core/testing';
import { ForosPage } from './foros.page';

describe('ForosPage', () => {
  let component: ForosPage;
  let fixture: ComponentFixture<ForosPage>;

  beforeEach(() => {
    fixture = TestBed.createComponent(ForosPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
