//Expose a client to communicate with python funcitons

const execute = (fnName='', fnParams={}, callback=()=>{}) => {
  const fn = window.eel.handler
  fn({
    fnName,
    fnParams
  })(callback)
}

export const sayHello = (params, callback) => {
  execute('say_hello', params, callback)
}
