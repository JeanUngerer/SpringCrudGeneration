import { Component, OnInit } from '@angular/core';
import {of} from "rxjs";
import {distinctUntilChanged} from "rxjs/operators";

@Component({
  selector: 'app-top-nav',
  templateUrl: './top-nav.component.html',
  styleUrls: ['./top-nav.component.scss']
})
export class TopNavComponent implements OnInit{


  logged : boolean = false;
  constructor(

  ) {}

  ngOnInit(): void {

  }
  handleClickLogout() {
    this.logged = !this.logged;
  //logout
  }





}
