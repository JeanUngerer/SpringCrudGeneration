import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {RouterModule, Routes} from "@angular/router";
import {AppComponent} from "./app.component";
import {HomeComponent} from "./components/layout/home/home.component";

const routes: Routes = [
  { path: 'home', component: HomeComponent},
	{ path: 'allbooks', loadChildren: () => import('./test/modules/allbooks/allbooks.module').then((m) => m.AllBooksModule), },
	{ path: 'allbooks', loadChildren: () => import('./test/modules/allbooks/allbooks.module').then((m) => m.AllBooksModule), },
	{ path: 'allbooks', loadChildren: () => import('./test/modules/allbooks/allbooks.module').then((m) => m.AllBooksModule), },
	{ path: 'allbooks', loadChildren: () => import('./test/modules/allbooks/allbooks.module').then((m) => m.AllBooksModule), },
	{ path: 'allbooks', loadChildren: () => import('./test/modules/allbooks/allbooks.module').then((m) => m.AllBooksModule), },
	{ path: 'message', loadChildren: () => import('./test/modules/message/message.module').then((m) => m.MessageModule), },
	{ path: 'rental', loadChildren: () => import('./test/modules/rental/rental.module').then((m) => m.RentalModule), },
	{ path: 'user', loadChildren: () => import('./test/modules/user/user.module').then((m) => m.UserModule), },
	{ path: 'allbooks', loadChildren: () => import('./test/modules/allbooks/allbooks.module').then((m) => m.AllBooksModule), },
	{ path: 'message', loadChildren: () => import('./test/modules/message/message.module').then((m) => m.MessageModule), },
	{ path: 'rental', loadChildren: () => import('./test/modules/rental/rental.module').then((m) => m.RentalModule), },
	{ path: 'user', loadChildren: () => import('./test/modules/user/user.module').then((m) => m.UserModule), },
	{ path: '', redirectTo: 'home', pathMatch: 'full' },

]

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    RouterModule.forRoot(routes)
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
