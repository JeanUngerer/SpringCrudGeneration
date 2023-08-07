import { NgModule } from '@angular/core';
import {MatTableModule} from "@angular/material/table";
import {AllBooksRoutingModule} from "./allbooks-routing.module";
import {AllBooksListComponent} from "./allbookslist/AllBookslist.component";

@NgModule({
	declarations: [
    AllBooksListComponent
	],
  imports : [
    MatTableModule,
    AllBooksRoutingModule
  ],
	exports: [
	]
})
export class AllBooksModule { }
