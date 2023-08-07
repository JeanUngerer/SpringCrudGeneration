import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import {TopNavComponent} from "./components/layout/top-nav/top-nav.component";
import { AppRoutingModule } from './app-routing.module';
import { AllBooksModule } from './test/modules/allbooks/allbooks.module';
import { HomeComponent } from './components/layout/home/home.component';

@NgModule({
  declarations: [
    AppComponent,
    TopNavComponent,
    HomeComponent,
  ],
  imports: [
    AllBooksModule,
    BrowserModule,
    AppRoutingModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule { }
