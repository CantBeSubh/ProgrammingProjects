import './style.css'
import * as THREE from 'three'

const scene= new THREE.Scene() //Scene

const box=new THREE.BoxGeometry(1,1,1)//Red cube
const material=new THREE.MeshBasicMaterial({color:'red'})
const mesh=new THREE.Mesh(box,material)
scene.add(mesh)

//Camera
const sizes={width:800,height:600}
const camera=new THREE.PerspectiveCamera(75,
    sizes.width/sizes.height
)
camera.position.z=3
camera.position.y=1
camera.position.x=1
scene.add(camera)

//renderer
const canvas=document.querySelector('.webgl')
const renderer=new THREE.WebGLRenderer({canvas})
renderer.setSize(sizes.width,sizes.height)

renderer.render(scene,camera)