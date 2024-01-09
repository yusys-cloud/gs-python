package com.demo;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * @author demo
 * @date 2021-11-08 14:02:56
 */
@Api(tags = "组件信息表")
@RestController
@RequestMapping("/api/xpcomponent")
public class XpComponentController {
    @Autowired
    private XpComponentService xpComponentService;

    /**
     * 组件全部查询接口
     *
     * @param xpComponentQueryVo 组件查询条件对象
     * @return ResultDto 返回数据
     */
    @ApiOperation("查询全部组件")
    @GetMapping("/")
    public ResultDto<List<XpComponentQueryVo>> listAllCmpWithoutProps(XpComponentQueryVo xpComponentQueryVo) {
        LambdaQueryWrapper<XpComponentEntity> wrapper = Wrappers.lambdaQuery(XpComponentEntity.class)
                .like(StringUtils.nonEmpty(xpComponentQueryVo.getCmpType()), XpComponentEntity::getCmpType, xpComponentQueryVo.getCmpType())
                .like(StringUtils.nonEmpty(xpComponentQueryVo.getCmpCode()), XpComponentEntity::getCmpCode, xpComponentQueryVo.getCmpCode())
                .like(StringUtils.nonEmpty(xpComponentQueryVo.getCmpName()), XpComponentEntity::getCmpName, xpComponentQueryVo.getCmpName())
                .eq(XpComponentEntity::getIsEnable, "Y").orderByAsc(XpComponentEntity::getCmpId);
        List<XpComponentEntity> list = xpComponentService.list(wrapper);
        List<XpComponentQueryVo> voList = new ArrayList<>();
        for (XpComponentEntity cmp : list) {
            voList.add(xpComponentService.cmpToVo(cmp));
        }
        return ResultDto.success(voList);
    }

    /**
     * 查询可被继承的组件
     *
     * @param xpComponentQueryVo 组件查询条件对象
     * @return ResultDto 返回数据
     */
    @ApiOperation("查询可被继承的组件")
    @GetMapping("/inherited/all")
    public ResultDto<List<XpComponentEntity>> listAllInheritedCmps(XpComponentQueryVo xpComponentQueryVo) {
        LambdaQueryWrapper<XpComponentEntity> wrapper = Wrappers.lambdaQuery(XpComponentEntity.class)
                .like(StringUtils.nonEmpty(xpComponentQueryVo.getCmpType()), XpComponentEntity::getCmpType, xpComponentQueryVo.getCmpType())
                .like(StringUtils.nonEmpty(xpComponentQueryVo.getCmpCode()), XpComponentEntity::getCmpCode, xpComponentQueryVo.getCmpCode())
                .like(StringUtils.nonEmpty(xpComponentQueryVo.getCmpName()), XpComponentEntity::getCmpName, xpComponentQueryVo.getCmpName())
                .eq(XpComponentEntity::getIsEnable, "Y").orderByAsc(XpComponentEntity::getCmpId)
                .and(wapr -> wapr.eq(XpComponentEntity::getInheritCmpId, "").or().isNull(XpComponentEntity::getInheritCmpId));
        List<XpComponentEntity> list = xpComponentService.list(wrapper);
        return ResultDto.success(list);
    }

    /**
     * 全部查询
     *
     * @param xpComponentQueryVo 组件查询条件对象
     */
    @ApiOperation("全部查询（包含组件的属性）")
    @GetMapping("/all")
    public ResultDto<List<XpComponentVoWithProps>> listAllCmpWithProps(XpComponentQueryVo xpComponentQueryVo) {
        return ResultDto.success(xpComponentService.listAllCmpWithProps(xpComponentQueryVo));
    }

    /**
     * 列表查询
     *
     * @param xpComponentQueryVo 组件查询条件对象
     */
    @ApiOperation("列表查询")
    @GetMapping("/list")
    public ResultDto<List<XpComponentQueryVo>> list(XpComponentQueryVo xpComponentQueryVo) {
        IPage<XpComponentQueryVo> page = xpComponentService.queryPage(xpComponentQueryVo);
        return ResultDto.success(page.getRecords()).total(page.getTotal());
    }

    /**
     * 详细
     *
     * @param id 组件id
     */
    @ApiOperation("详细")
    @GetMapping("/info/{id}")
    public ResultDto<XpComponentQueryVo> info(@PathVariable("id") String id) {
        XpComponentEntity xpComponent = xpComponentService.getById(id);
        return ResultDto.success(xpComponentService.cmpToVo(xpComponent));
    }

    /**
     * 保存
     *
     * @param xpComponent 组件对象
     */
    @ApiOperation("保存")
    @PostMapping("/save")
    public ResultDto<Boolean> save(@RequestBody XpComponentQueryVo xpComponent) {
        return ResultDto.success(xpComponentService.save(new XpComponentEntity(xpComponent)));
    }

    /**
     * 修改
     *
     * @param xpComponent 组件对象
     */
    @ApiOperation("修改")
    @PostMapping("/update")
    public ResultDto<Boolean> update(@RequestBody XpComponentQueryVo xpComponent) {
        return ResultDto.success(xpComponentService.updateById(new XpComponentEntity(xpComponent)));
    }

    /**
     * 删除
     *
     * @param ids 删除对象id数组
     */
    @ApiOperation("删除")
    @PostMapping("/delete")
    public ResultDto<Boolean> delete(@RequestBody String[] ids) {
        return ResultDto.success(xpComponentService.removeByIds(Arrays.asList(ids)));
    }

}