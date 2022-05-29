const scene= new THREE.Scene() //Scene

const box=new THREE.BoxGeometry(1,1,1)//Red cube
const material=new THREE.MeshBasicMaterial({color:'red'})
const mesh=new THREE.Mesh(box,material)
// mesh.scale.x =0.5
scene.add(mesh)

//axis-helper
const axesHelper=new THREE.AxisHelper(2)
scene.add(axesHelper)
//Camera
const sizes={width:800,height:600}
const camera=new THREE.PerspectiveCamera(75,
    sizes.width/sizes.height
)
camera.position.z=3
camera.position.y=1
camera.position.x=1
// camera.rotation.y= Math.PI
scene.add(camera)

//renderer
const canvas=document.querySelector('.webgl')
const renderer=new THREE.WebGLRenderer({canvas})
renderer.setSize(sizes.width,sizes.height)

renderer.render(scene,camera)