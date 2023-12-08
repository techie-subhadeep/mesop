from pydantic import validate_arguments

import optic.protos.ui_pb2 as pb
import optic.components.box.box_pb2 as box_pb
from optic.component_helpers import ComponentWithChildren


@validate_arguments
def box(
  *,
  background_color: str = "",
  key: str | None = None,
):
  """
  This function creates a box.

  Args:
      label (str): The text to be displayed
  """
  return ComponentWithChildren(
    component=pb.Component(
      key=pb.Key(key=key or ""),
      type=pb.Type(
        name="box",
        value=box_pb.BoxType(
          background_color=background_color
        ).SerializeToString(),
      ),
    ),
  )
