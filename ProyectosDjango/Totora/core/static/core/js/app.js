window.addEventListener('load', ()=> {
    let lon
    let lat

    let temperaturaValor = document.getElementById('temperatura-valor')  
    let temperaturaDescripcion = document.getElementById('temperatura-descripcion')  
    
    let ubicacion = document.getElementById('ubicacion')  
    let iconoAnimado = document.getElementById('icono-animado') 

    if(navigator.geolocation){
       navigator.geolocation.getCurrentPosition( posicion => {
           //console.log(posicion.coords.latitude)
           lon = posicion.coords.longitude
           lat = posicion.coords.latitude
            //ubicación actual    
           const url = `https://api.openweathermap.org/data/2.5/weather?units=metric&lang=es&lat=${lat}&lon=${lon}&appid=b85bf1a0b584dfb63ab628d984895c0d`
           
           //const url = `https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=b85bf1a0b584dfb63ab628d984895c0d`

           //console.log(url)

           fetch(url)
            .then( response => { return response.json()})
            .then( data => {
                //console.log(data)
                
                let temp = Math.round(data.main.temp)
                //console.log(temp)
                temperaturaValor.textContent = `${temp} ° C`

                //console.log(data.weather[0].description)
                let desc = data.weather[0].description
                temperaturaDescripcion.textContent = desc[0].toUpperCase() + desc.slice(1)
                ubicacion.textContent = data.name
			   
			   
                //para iconos estáticos
                //const urlIcon = `http://openweathermap.org/img/wn/${iconCode}.png`                     
                //icono.src = urlIcon
                //console.log(data.weather[0].icon)

                //para iconos dinámicos
                console.log(data.weather[0].main)
                switch (data.weather[0].main) {
                    case 'Thunderstorm':
                      iconoAnimado.src='/core/static/core/animated/thunder.svg'
                      console.log('Tormenta');
                      break;
                    case 'Drizzle':
                      iconoAnimado.src='/core/static/core/animated/rainy-2.svg'
                      console.log('Llovizna');
                      break;
                    case 'Rain':
                      iconoAnimado.src='/core/static/core/animated/rainy-7.svg'
                      console.log('Lluvia');
                      break;
                    case 'Snow':
                      iconoAnimado.src='/core/static/core/animated/snowy-6.svg'
                        console.log('Nieve');
                      break;                        
                    case 'Clear':
                        iconoAnimado.src='/core/static/core/animated/day.svg'
                        console.log('Limpio');
                      break;
                    case 'Atmosphere':
                      iconoAnimado.src='/core/static/core/animated/weather.svg'
                        console.log('Atmosfera');
                        break;  
                    case 'Clouds':
                        iconoAnimado.src='/core/static/core/animated/cloudy.svg'
                        console.log('Nubes');
                        break;  
                    default:
                      iconoAnimado.src='/core/static/core/animated/cloudy-day-1.svg'
                      console.log('por defecto');
                  }

            })
            .catch( error => {
                console.log(error)
            })
       })
          
    }
})
