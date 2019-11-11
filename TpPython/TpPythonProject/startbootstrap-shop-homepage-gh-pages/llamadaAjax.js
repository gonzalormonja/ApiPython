/*document.querySelector('#test').addEventListener('click',function(){
	obtenerProductosTotales();
});*/

function seleccionarCategoria(id){
	let url = "http://127.0.0.1:8000/1111/productosCategoria/"+id+"/";
	const api = new XMLHttpRequest();
	api.open('GET',url,true);
	api.send();

	api.onreadystatechange = function(){
		if(this.status==200 && this.readyState == 4){
			datos = JSON.parse(this.responseText);
			let resultado = document.querySelector('#resultado');
			resultado.innerHTML = '';
			for(let item of datos){
				resultado.innerHTML += '<div class="col-lg-4 col-md-6 mb-4">'+
				'<div class="card h-100">'+
	              '<img class="card-img-top" src="'+item.fotos[0]+'" alt="">'+
	              '<div class="card-body">'+
	                '<h4 class="card-title">'+
	                 '<a>'+item.nombre+'</a>'+
	                '</h4>'+
	                '<div class="row">'+
	                '<h5 class="col-7">$'+item.precio+'</h5>'+
	                '<button type="button" class="btn btn-primary col-5"  data-toggle="modal" data-target="#modalQuickView" onclick="verProducto('+item.id+')">Ver mas</button>'+
	                '</div>'+
	              '</div>'+
	              '<div class="card-footer">'+
	                '<small class="text-muted">&#9733; &#9733; &#9733; &#9733; &#9734;</small>'+
	              '</div>'+
	            '</div>'+
	          '</div>';
			}
		}
	}
}

window.onload=function() {
	obtenerProductosTotales();
	obtenerCategorias();
}

function obtenerCategorias(){
	let url = "http://127.0.0.1:8000/2222/categorias/";
	const api = new XMLHttpRequest();
	api.open('GET',url,true);
	api.send();
	api.onreadystatechange = function(){
		if(this.status==200 && this.readyState == 4){
			datos = JSON.parse(this.responseText);
			let resultado = document.querySelector('#categorias');
			resultado.innerHTML = '';
			for(let item of datos){
				resultado.innerHTML+='<a onclick="seleccionarCategoria(this.id)"id="'+item.id+'" href="#" class="list-group-item">'+item.nombre+'</a>';
			}
		}
	}
}

function obtenerProductosTotales(){
	let url = "http://127.0.0.1:8000/2222/productos/";
	const api = new XMLHttpRequest();
	api.open('GET',url,true);
	api.send();

	api.onreadystatechange = function(){
		if(this.status==200 && this.readyState == 4){
			datos = JSON.parse(this.responseText);
			console.log(datos);
			let resultado = document.querySelector('#resultado');
			resultado.innerHTML = '';
			for(let item of datos){
				resultado.innerHTML += '<div class="col-lg-4 col-md-6 mb-4">'+
				'<div class="card h-100">'+
	              '<img class="card-img-top" src="'+item.fotos[0]+'" alt="">'+
	              '<div class="card-body">'+
	                '<h4 class="card-title">'+
	                 '<a>'+item.nombre+'</a>'+
	                '</h4>'+
	                '<div class="row">'+
	                '<h5 class="col-7">$'+item.precio+'</h5>'+
	                '<button type="button" class="btn btn-primary col-5"  data-toggle="modal" data-target="#modalQuickView" onclick="verProducto('+item.id+')">Ver mas</button>'+
	                '</div>'+
	              '</div>'+
	              '<div class="card-footer">'+
	                '<small class="text-muted">&#9733; &#9733; &#9733; &#9733; &#9734;</small>'+
	              '</div>'+
	            '</div>'+
	          '</div>';
			}
		}
	}
}

function verProducto(id){
	let url = "http://127.0.0.1:8000/2222/productos/"+id+"/";
	const api = new XMLHttpRequest();
	api.open('GET',url,true);
	api.send();

	api.onreadystatechange = function(){
		if(this.status==200 && this.readyState == 4){
			datos = JSON.parse(this.responseText);
			document.getElementById("precio").innerHTML = "$"+datos.precio;
			document.getElementById("nombre").innerHTML = datos.nombre;
			document.getElementById("descripcion").innerHTML = datos.descripcion;
			let resp = document.querySelector('#fotosModal');
			resp.innerHTML = "";
			let i = 0;
			for(let foto of datos.fotos){
				if(i>0){
					resp.innerHTML+='<div class="carousel-item">'+
					'<img id="foto1" class="d-block w-100"'+
					'src="'+foto+'">'+
					'</div>';
				}else{
					resp.innerHTML+='<div class="carousel-item active">'+
					'<img id="foto1" class="d-block w-100"'+
					'src="'+foto+'">'+
					'</div>';
				}
				i++;
			}
		}
	}
}