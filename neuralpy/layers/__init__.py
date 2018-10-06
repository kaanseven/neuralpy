from neuralpy.layers.mlp import MLP
from neuralpy.layers.input_ import Input
import neuralpy.layers.layer as layer

mapping = {
    layer.type_mlp: MLP,
    layer.type_input: Input
}
