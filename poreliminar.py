def scheduleBranchDayTime(driver):
    try:
        wait = WebDriverWait(driver, 20)

        print("Paso 1: Esperando que el contenedor principal del formulario esté presente y visible...")
        wait.until(EC.presence_of_element_located((By.ID, "TABLE3")))
        print("TABLE3 está presente.")

        print("Paso 2: Esperando que el select de Sede ('vREGCONREG') sea VISIBLE...")
        # Cambiamos a visibility_of_element_located, que es menos estricto que clickeable
        branchLists = wait.until(
            EC.visibility_of_element_located((By.ID, "vREGCONREG"))
        )
        print("Elemento 'vREGCONREG' es visible.")

        if not branchLists.is_enabled():
            print("Elemento 'vREGCONREG' visible pero NO habilitado para interactuar. Intentando habilitar con JS...")
            # Intenta habilitar el elemento con JavaScript si está deshabilitado
            driver.execute_script("arguments[0].removeAttribute('disabled');", branchLists)
            print("Intento de habilitar 'vREGCONREG' con JS.")
            # Re-obtener el elemento si se modificó su estado, o esperar un momento
            time.sleep(1) # Pequeña pausa para que el cambio de JS surta efecto

        print("Paso 2.1: Intentando seleccionar Sede con JavaScript...")
        # Seleccionar por valor '28' (ENVIGADO) y disparar el evento 'change'
        driver.execute_script("arguments[0].value = '28';", branchLists)
        driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", branchLists)
        print("Selección de Sede (ENVIGADO) realizada correctamente con JavaScript.")
        time.sleep(2) # Pausa para que cualquier JS asociado al cambio de sede se ejecute

        # --- Para el Día ---
        print("Paso 3: Esperando que el select de Día ('vDIA') sea VISIBLE...")
        daySelectElement = wait.until(
            EC.visibility_of_element_located((By.ID, "vDIA"))
        )
        print("Elemento del Día ('vDIA') es visible.")
        
        if not daySelectElement.is_enabled():
            print("Elemento 'vDIA' visible pero NO habilitado para interactuar. Intentando habilitar con JS...")
            driver.execute_script("arguments[0].removeAttribute('disabled');", daySelectElement)
            print("Intento de habilitar 'vDIA' con JS.")
            time.sleep(1)

        print("Paso 3.1: Intentando seleccionar Día con JavaScript...")
        # Seleccionar por texto visible "Jueves 17/07/25"
        # Para seleccionar por texto visible con JS, es un poco más complejo,
        # lo más fácil es por valor si lo conoces, o iterar las opciones.
        # Basado en tu HTML, "Jueves 17/07/25" tiene value="5".
        driver.execute_script("arguments[0].value = '5';", daySelectElement)
        driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", daySelectElement)
        print("Selección de Día (Jueves 17/07/25) realizada correctamente con JavaScript.")
        time.sleep(2)

    except Exception as e:
        print(f"ERROR: Falló al encontrar o seleccionar los elementos: {e}")
        driver.save_screenshot("ERROR_screenshot_on_exception.png")
        with open("ERROR_page_source_on_exception.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        print("Captura de pantalla 'ERROR_screenshot_on_exception.png' y page_source 'ERROR_page_source_on_exception.html' guardados en caso de excepción.")